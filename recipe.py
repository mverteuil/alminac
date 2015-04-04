import re
import pprint

recipe_form_pattern = re.compile(r"add(?P<form_type>Recipe)\(new ItemStack(?P<form_yield>\(.*\)), new Object\[\] {(?P<form_method>.*)}\)")
shapeless_recipe_form_pattern = re.compile(r"add(?P<form_type>ShapelessRecipe)\(new ItemStack(?P<form_yield>\(.*\)), new Object\[\] {(?P<form_method>.*)}\)")
item_stack_pattern = re.compile(r"\((?:Items|Blocks)\.(?P<item>\w+)(?:|, (?P<quantity>\d+)(?:|, (?:|4 \+ )(?P<metadata>(\d|[a-zA-Z0-9._()]+))(?:| - 4)))\)")
shape_pattern = re.compile(r'"(.+?)"')
shaped_ingredient_pattern = re.compile(r"'(?P<symbol>.)', (?:new ItemStack|(?:Items|Blocks)(?:\.))(?P<ingredient>((?!Block)\w+|[()+-, a-zA-Z0-9._]+))")
shapeless_ingredient_pattern = re.compile(r"(?:new ItemStack|(?:Items|Blocks)(?:\.))(?P<ingredient>((?!Block)\w+|[()+-, a-zA-Z0-9._]+\)))")

formulae = []
if __name__ == '__main__':
    with open('recipes.txt', 'r') as recipe_file:
        recipe_lines = recipe_file.readlines()
    for recipe_line in recipe_lines:
        match = recipe_form_pattern.search(recipe_line)
        if match:
            formulae.append(match.groupdict())
        else:
            match = shapeless_recipe_form_pattern.search(recipe_line)
            if match:
                formulae.append(match.groupdict())


for formula in formulae:
    formula['form_yield'] = item_stack_pattern.search(formula['form_yield']).groupdict()
    if formula['form_type'] == 'Recipe':
        formula_shape = shape_pattern.findall(formula['form_method'])
        formula_ingredients = [(symbol, ingredient.strip())
                               for symbol, ingredient, _ in shaped_ingredient_pattern.findall(formula['form_method'])]
        formula['form_method'] = {
            'shape': formula_shape,
            'ingredients': formula_ingredients,
        }
    elif formula['form_type'] == 'ShapelessRecipe':
        formula['form_method'] = [(ingredient.strip())
                                  for ingredient, _ in shapeless_ingredient_pattern.findall(formula['form_method'])]



pprint.pprint(formulae)
