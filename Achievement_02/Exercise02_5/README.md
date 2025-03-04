# README for Exercise 2.5

## Overview
In **Exercise 2.5**, I worked on enhancing a Django project by implementing **class-based views (CBVs)**, managing **URL routing**, and improving **model relationships**. This exercise helped me gain a deeper understanding of Django's **views, templates, and ORM queries**.

---

## What I Did

### **Implemented Class-Based Views (CBVs)**
- Created `ListView` and `DetailView` for both **Recipes** and **Ingredients**.
- Used `get_context_data()` to pass related objects (e.g., linking `RecipeIngredient` to show related recipes for an ingredient).

### **Set Up URL Routing**
- Organized `urls.py` for `recipes` and `ingredients`, ensuring proper **namespace usage**.
- Fixed a **namespace conflict warning** by properly structuring `recipe_project/urls.py`.

### **Connected Multiple Models Using Queries**
- Retrieved **related recipes** for an ingredient using:
  ```python
  RecipeIngredient.objects.filter(ingredient=self.object)
  ```
- Used `reverse()` to dynamically generate URLs for **recipe detail pages**.

### **Managed Static Files**
- Used `{% static %}` in templates to load **CSS, JavaScript, and images**.
- Configured `STATIC_URL` and `STATICFILES_DIRS` in `settings.py`.

### **Wrote Unit Tests**
- Tested `get_absolute_url()` for **Recipe** and **Ingredient** models.
- Verified that **detail views return the correct response** and use the expected template.
