#!/usr/bin/env bash

# Minecraft 1.8 smelting mining tool
# Author: Matthew de Verteuil (http://www.github.com/mverteuil)

# Extract the smelting formulae from FurnaceRecipes.java... 
grep -Eo 'Smelting(Recipe)?(ForBlock)?(.*?, new ItemStack.*\))'                 \
    parts/mcp910/src/minecraft/net/minecraft/item/crafting/FurnaceRecipes.java  |
# ... and sort it
sort
