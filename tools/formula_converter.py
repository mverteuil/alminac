#!/usr/bin/env python
import pprint
import re
import sys

recipe_form_pattern = re.compile(r"add(?P<form_type>Recipe)\(new ItemStack(?P<form_yield>\(.*\)), new Object\[\] {(?P<form_method>.*)}\)")
shapeless_recipe_form_pattern = re.compile(r"add(?P<form_type>ShapelessRecipe)\(new ItemStack(?P<form_yield>\(.*\)), new Object\[\] {(?P<form_method>.*)}\)")
item_stack_pattern = re.compile(r"\((?:Items|Blocks)\.(?P<item>\w+)(?:|, (?P<quantity>\d+)(?:|, (?:|4 \+ )(?P<metadata>(\d|[a-zA-Z0-9._()]+))(?:| - 4)))\)")
item_metadata_pattern = re.compile(r"(?P<metadata>^\d|[A-Z]{1}[A-Z_]+)")
shape_pattern = re.compile(r'"(?P<shape>.{1,3})"')
shaped_ingredient_pattern = re.compile(r"'(?P<symbol>.)', (?:new ItemStack|(?:Items|Blocks)(?:\.))(?P<ingredient>((?!Block)\w+|[()+-, a-zA-Z0-9._]+))")
shapeless_ingredient_pattern = re.compile(r"(?:new ItemStack|(?:Items|Blocks)(?:\.))(?P<ingredient>((?!Block)\w+|[()+-, a-zA-Z0-9._]+\)))")

def parse_ingrendient_and_normalize(ingredient_string):
    """ Parses and ingredient strings and normalizes to dicts. """
    # Sanitize first
    cleaned_ingredient_string = ingredient_string.strip()
    # ItemStack format
    if item_stack_pattern.search(cleaned_ingredient_string):
        ingredient = item_stack_pattern.search(cleaned_ingredient_string).groupdict()
        if ingredient['metadata']:
            ingredient['metadata'] = item_metadata_pattern.search(ingredient['metadata']).group(1)


    elif map(str.isalpha, cleaned_ingredient_string.split('_')):
        ingredient = {'item': cleaned_ingredient_string.strip(),
                      'quantity': '1',
                      'metadata': None}
    return ingredient

# use stdin if it's full
if not sys.stdin.isatty():
    input_stream = sys.stdin.readlines()

# otherwise, read the given filename
else:
    try:
        input_filename = sys.argv[1]
        with open(input_filename, 'rU') as input_file:
            input_stream = input_file.readlines()
    except IndexError:
        print "Expected line data on stdin or a filename argument."
        sys.exit(1)


# Match and normalize the input stream lines into a common format
FORMULA_MATCHERS = (recipe_form_pattern, shapeless_recipe_form_pattern, )
formulae = []
for formula_line in input_stream:
    for formula_matcher in FORMULA_MATCHERS:
        if formula_matcher.match(formula_line):
            formulae.append(formula_matcher.match(formula_line).groupdict())
        else:
            continue

# Perform secondary reshaping of data into entirely normalized format
for formula in formulae:
    formula['form_yield'] = parse_ingrendient_and_normalize(formula['form_yield'])
    if formula['form_type'] == 'Recipe':
        formula_shape = shape_pattern.findall(formula['form_method'])
        formula_ingredients = {symbol: parse_ingrendient_and_normalize(ingredient)
                               for symbol, ingredient, _ in shaped_ingredient_pattern.findall(formula['form_method'])}
        formula['form_method'] = {
            'shape': formula_shape,
            'ingredients': formula_ingredients,
        }
    elif formula['form_type'] == 'ShapelessRecipe':
        formula['form_method'] = [parse_ingrendient_and_normalize(ingredient)
                                  for ingredient, _ in shapeless_ingredient_pattern.findall(formula['form_method'])]

# Demonstrate the transformation
pprint.pprint(formulae)
