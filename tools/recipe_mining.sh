#!/usr/bin/env bash

# Minecraft 1.8 recipe mining tool
# Author: Matthew de Verteuil (http://www.github.com/mverteuil)

# Extract the individual recipes from CraftingManager.java...
grep -Eo "add(ShapelessRecipe|Recipe)\(new ItemStack.*\)"                       \
    parts/mcp910/src/minecraft/net/minecraft/item/crafting/CraftingManager.java |
# ... and sort it
sort
