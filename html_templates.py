import textwrap

def get_recipe_display_html(name, views, created_at, servings, font_size, ingredients_html, instructions_html):
    """Returns the HTML for the detailed recipe paper view."""
    # NOTE: We use var(--text-main) so the text color adapts to Dark Mode automatically
    # Added: Servings display in the meta section
    return f"""
<div class="recipe-paper">
<div class="recipe-header">{name}</div>
<div class="recipe-meta">
👀 Viewed {views} times &nbsp;•&nbsp; 🥘 {servings} Servings &nbsp;•&nbsp; 📅 {created_at.strftime('%b %d, %Y')}
</div>
<br>
<div class="recipe-section">
<div class="section-title">Ingredients</div>
<div style="font-size: {font_size}px; line-height: 1.6; color: var(--text-main);">
{ingredients_html}
</div>
</div>
<div class="recipe-section">
<div class="section-title">Instructions</div>
<div style="font-size: {font_size}px; line-height: 1.6; color: var(--text-main);">
{instructions_html}
</div>
</div>
</div>
"""

def get_trending_card_html(emoji, name, views):
    """Returns the HTML for the Apple-style trending/favorite cards."""
    return f"""
<div class="emoji-img">{emoji}</div>
<span class="apple-tag">Favorite</span>
<div class="apple-title">{name}</div>
<div class="apple-desc">{views} times you have viewed this recipe</div>
"""
