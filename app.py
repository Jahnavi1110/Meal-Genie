import streamlit as st
from google import genai
import pymysql.cursors
from datetime import datetime
import html_templates
import os
from dotenv import load_dotenv
load_dotenv()

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Meal Genie", layout="centered")


# --- 2. LOAD BASE CSS ---
def local_css(file_name):
    if not os.path.exists(file_name):
        st.error(f"🚨 CSS ERROR: Could not find '{file_name}'.")
        return
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")

# --- 3. THEME MANAGEMENT & FIXES ---
st.sidebar.header("⚙️ Settings")
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

if dark_mode:
    # --- DARK MODE CSS ---
    st.markdown("""
    <style>
        :root {
            --app-bg: #0E1117;
            --text-main: #f0f2f6;
            --text-secondary: #b0b0b0;

            --card-bg: #1e1e1e;
            --card-hover: #2d2d2d;
            --card-shadow: rgba(0,0,0,0.4);
            --card-border: #333;

            --paper-bg: #151515;
            --paper-border: #333;
            --section-bg: #1e1e1e;
            --section-border: #444;

            --header-bg: rgba(14, 17, 23, 0.9);
            --header-border: rgba(255,255,255,0.1);

            --tag-color: #ffae42;
            --btn-bg: #2d2d2d;
            --btn-text: #ffffff;
            --btn-border: #444;
            --btn-hover: #FA9200;
            --btn-hover-text: #ffffff;
        }

        .stApp { background-color: var(--app-bg) !important; }
        section[data-testid="stSidebar"] { background-color: #151517 !important; border-right: 1px solid #333; }
        h1, h2, h3, p, span, div { color: var(--text-main) !important; }

        /* --- FIX ALL INPUTS (Including MultiSelect) --- */
        .stTextInput > div > div > input, 
        .stTextArea > div > div > textarea, 
        .stSelectbox > div > div > div, 
        .stMultiSelect > div > div > div,  /* <--- THIS WAS MISSING! */
        .stNumberInput > div > div > input {
            background-color: #2d2d2d !important; 
            color: white !important; 
            border-color: #444 !important;
        }

        /* Placeholder Text Fix */
        .stTextInput input::placeholder, .stTextArea textarea::placeholder { color: #666 !important; }

        /* --- DROPDOWN MENUS --- */
        div[data-baseweb="popover"] > div, div[data-baseweb="menu"], li[role="option"] {
            background-color: #1e1e1e !important; color: white !important;
        }
        li[role="option"]:hover, li[role="option"][aria-selected="true"] {
            background-color: #FA9200 !important; color: white !important;
        }

        /* MultiSelect Tags (The items you select) */
        span[data-baseweb="tag"] { 
            background-color: #444 !important; 
        }
        span[data-baseweb="tag"] span { 
            color: white !important; 
        }

        /* Header */
        header[data-testid="stHeader"] { background-color: transparent !important; z-index: 100000 !important; }
        header[data-testid="stHeader"] button { color: white !important; }
        header[data-testid="stHeader"] button svg { fill: white !important; }
    </style>
    """, unsafe_allow_html=True)

else:
    # --- LIGHT MODE CSS ---
    st.markdown("""
    <style>
        :root {
            --app-bg: #ffffff;
            --text-main: #1d1d1f;
            --text-secondary: #86868b;
            --card-bg: #f5f5f7;
            --card-hover: #ffffff;
            --card-shadow: rgba(0,0,0,0.1);
            --card-border: transparent;
            --paper-bg: #ffffff;
            --paper-border: #eee;
            --section-bg: #fafafa;
            --section-border: #e0e0e0;
            --header-bg: rgba(255, 255, 255, 0.95);
            --header-border: rgba(0,0,0,0.05);
            --btn-bg: #ffffff;
            --btn-text: #0071e3;
            --btn-border: #0071e3;
            --btn-hover: #0071e3;
            --btn-hover-text: #ffffff;
        }
        header[data-testid="stHeader"] { background-color: transparent !important; z-index: 100000 !important; }
        header[data-testid="stHeader"] button { color: #1d1d1f !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. CONFIGURATION ---
API_KEY = os.getenv("GEMINI_API_KEY")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "cursorclass": pymysql.cursors.DictCursor
}


# --- 5. SETUP & MIGRATION ---
@st.cache_resource
def setup_client():
    try:
        return genai.Client(api_key=API_KEY)
    except:
        return None


client = setup_client()
MODEL = "gemini-2.5-flash"


def get_db_connection():
    try:
        return pymysql.connect(**DB_CONFIG)
    except Exception as e:
        st.error(f"DB Connection Error: {e}"); return None


def check_and_update_db():
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SHOW COLUMNS FROM recipes LIKE 'servings'")
                if not cursor.fetchone():
                    cursor.execute("ALTER TABLE recipes ADD COLUMN servings INT DEFAULT 2")
                    conn.commit()
        except Exception:
            pass
        finally:
            conn.close()


check_and_update_db()


def run_query(query, params=None, fetch=False):
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                if fetch: return cursor.fetchall()
                conn.commit()
        except Exception:
            pass
        finally:
            conn.close()
    return None


def get_food_emoji(name):
    name = name.lower()
    if "pancake" in name: return "🥞"
    if "egg" in name: return "🍳"
    if "pasta" in name or "spaghetti" in name or "noodle" in name: return "🍝"
    if "rice" in name: return "🍚"
    if "chicken" in name: return "🍗"
    if "salad" in name: return "🥗"
    if "burger" in name: return "🍔"
    if "pizza" in name: return "🍕"
    if "cake" in name: return "🍰"
    return "🍽️"


# --- 6. LOGIC HELPERS ---
def generate_recipe(ingredients_list, cuisine, restrictions, servings):
    ingredients_str = ", ".join(ingredients_list)
    cuisine_text = f"Style: {cuisine}." if cuisine != 'Any' else ""
    restriction_text = f"Restrictions: {', '.join(restrictions)}." if restrictions else ""

    prompt = f"""
    You are an expert AI Chef. Create a recipe for {servings} servings using: {ingredients_str}.
    {cuisine_text} {restriction_text}
    Important: Adjust quantities for exactly {servings} servings.
    Output Format:
    # Recipe Name
    **Ingredients:** ...
    **Instructions:** ...
    """
    if not client: return "Error: AI Busy."
    try:
        response = client.models.generate_content(model=MODEL, contents=prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"


def format_to_html_list(text, list_type="ul", split_by_comma=True):
    clean_text = text.replace('*', '').replace('-', '').strip()
    if '\n' in clean_text:
        items = [x.strip() for x in clean_text.split('\n') if x.strip()]
    elif split_by_comma:
        items = [x.strip() for x in clean_text.split(',') if x.strip()]
    else:        items = [clean_text]

    text_color = "var(--text-main)"

    if list_type == "plain":
        html = "<div style='margin-top: 5px;'>"
        for item in items:
            html += f"<div style='margin-bottom: 12px; color: {text_color} !important;'>{item}</div>"
        html += "</div>"
        return html

    html = f"<{list_type} style='padding-left: 20px; margin-top: 5px; margin-bottom: 0; color: {text_color} !important;'>"
    for item in items:
        html += f"<li style='margin-bottom: 8px;'>{item}</li>"
    html += f"</{list_type}>"
    return html


def parse_and_display_recipe(recipe_obj, font_size):
    full_text = recipe_obj['output']
    if full_text.strip().startswith('#'):
        full_text = "\n".join(full_text.split('\n')[1:])

    parts = full_text.split('**Instructions:**')
    ing_text = parts[0].replace('**Ingredients:**', '').strip() if len(parts) > 0 else "N/A"
    inst_text = parts[1].strip() if len(parts) > 1 else full_text

    final_ing_html = format_to_html_list(ing_text, "ul", split_by_comma=True)
    final_inst_html = format_to_html_list(inst_text, "plain", split_by_comma=False)

    servings_count = recipe_obj.get('servings', 2)
    if servings_count is None: servings_count = 2

    st.markdown(
        html_templates.get_recipe_display_html(
            name=recipe_obj['name'],
            views=recipe_obj.get('view_count', 'New'),
            created_at=recipe_obj['created_at'],
            servings=servings_count,
            font_size=font_size,
            ingredients_html=final_ing_html,
            instructions_html=final_inst_html
        ),
        unsafe_allow_html=True
    )


# --- 7. APP LAYOUT ---

if 'active_recipe' not in st.session_state: st.session_state['active_recipe'] = None
if 'temp_recipe' not in st.session_state: st.session_state['temp_recipe'] = None

# Sticky Header
st.markdown("""
    <div class="sticky-header">
        <div class="header-title">
            <span>Meal Genie</span> 🧞‍♂️
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar History
st.sidebar.header("Recent History")
history_data = run_query("SELECT * FROM recipes ORDER BY created_at DESC LIMIT 10", fetch=True)
if history_data:
    for recipe in history_data:
        if st.sidebar.button(f" {recipe['name']}", key=f"hist_{recipe['id']}"):
            run_query("UPDATE recipes SET view_count = view_count + 1 WHERE id = %s", (recipe['id'],))
            st.session_state['active_recipe'] = recipe
            st.session_state['temp_recipe'] = None
            st.rerun()

# Main Logic
if st.session_state['temp_recipe']:
    st.info("✨ Recipe Generated! Review it below.")
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("⬅ Back"):
            st.session_state['temp_recipe'] = None
            st.rerun()
    with col2:
        if st.button("✅ Done (Save to History)", type="primary", use_container_width=True):
            r = st.session_state['temp_recipe']
            run_query(
                "INSERT INTO recipes (name, ingredients, output, servings, view_count, created_at) VALUES (%s, %s, %s, %s, 1, %s)",
                (r['name'], r['ingredients'], r['output'], r['servings'], r['created_at'])
            )
            st.success("Recipe Saved!")
            st.session_state['temp_recipe'] = None
            st.rerun()

    font_size = st.slider("Text Size", 14, 24, 18)
    parse_and_display_recipe(st.session_state['temp_recipe'], font_size)

elif st.session_state['active_recipe']:
    # VIEW SAVED RECIPE
    col_back, col_spacer, col_delete = st.columns([1, 2, 1])
    with col_back:
        if st.button("← Back"):
            st.session_state['active_recipe'] = None
            st.rerun()
    with col_delete:
        if st.button("🗑️ Delete", type="primary"):
            rec_id = st.session_state['active_recipe']['id']
            run_query("DELETE FROM recipes WHERE id = %s", (rec_id,))
            st.session_state['active_recipe'] = None
            st.rerun()

    font_size = st.slider("Text Size", 14, 24, 18)
    parse_and_display_recipe(st.session_state['active_recipe'], font_size)

else:
    # HOME PAGE
    st.markdown("### 🍳 Explore the Kitchen")

    col1, col2 = st.columns(2)
    with col1:
        cuisine = st.selectbox("Cuisinee...haha", ('Any', 'Chinese', 'Italian', 'Mexican', 'Indian', 'Thai'))
    with col2:
        restrictions = st.multiselect("Dietary..oops", ['Non-Vegetarian', 'Vegetarian', 'Gluten-Free', 'Keto', 'SeaFood'])

    servings = st.slider("How many to Serve?", 1, 10, 2)
    ingredients_input = st.text_area("Ingredients", placeholder="What's up Human! What do you have in your kitchen today? (e.g. egg, bread)", height=100)

    if st.button("Wish for a Recipe!", type="primary", use_container_width=True):
        if not ingredients_input:
            st.error("Please enter ingredients!")
        else:
            with st.spinner('Genie 🧞‍♂️ is designing your dish...'):
                ing_list = [x.strip() for x in ingredients_input.split(',')]
                output = generate_recipe(ing_list, cuisine, restrictions, servings)
                name = output.split('\n')[0].replace('#', '').strip() or "New Recipe"
                ing_str = ", ".join(ing_list)

                st.session_state['temp_recipe'] = {
                    'name': name,
                    'ingredients': ing_str,
                    'output': output,
                    'servings': servings,
                    'created_at': datetime.now()
                }
                st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### Favorite Recipes")

    top_recipes = run_query("SELECT * FROM recipes ORDER BY view_count DESC LIMIT 3", fetch=True)

    if top_recipes:
        cols = st.columns(3)
        for i, recipe in enumerate(top_recipes):
            with cols[i]:
                st.markdown(
                    html_templates.get_trending_card_html(
                        emoji=get_food_emoji(recipe['name']),
                        name=recipe['name'],
                        views=recipe['view_count']
                    ),
                    unsafe_allow_html=True
                )
                if st.button("View Recipe", key=f"card_btn_{recipe['id']}"):
                    run_query("UPDATE recipes SET view_count = view_count + 1 WHERE id = %s", (recipe['id'],))
                    st.session_state['active_recipe'] = recipe
                    st.rerun()
    else:
        st.info("👀 No favorites yet! Create a recipe and save it to see it here.")
