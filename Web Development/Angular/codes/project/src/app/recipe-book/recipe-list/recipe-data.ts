import { Ingredient } from "src/app/shared/ingredient.model";
import { Recipe } from "../recipe.model";

export const recipes: Recipe[] = [
    new Recipe(
      "Hamburger",
      "No more dry, lackluster hamburgers. These are juicy, and spices can be easily added or changed to suit anyone's taste. If you find the meat mixture too mushy, just add more bread crumbs until it forms patties that hold their shape. ",
      "https://www.allrecipes.com/thmb/49Srz_vFJmmg40yDTfkoFdb8y7M=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/49404-juiciest-hamburgers-ever-DDMFS-4x3-86fc27c741dd410aa365f96490c54060.jpg",
      [
        new Ingredient("Lean Ground Beef", "1.5 pounds"),
        new Ingredient("Finely Chopped Onion", "0.5"),
        new Ingredient("Shredded Cheddar Cheese", "0.5 cup"),
        new Ingredient("Egg", "1"),
        new Ingredient("Envelope Dry Onion Soup Mix", "1 ounce"),
        new Ingredient("Minced Garlic", "1 clove"),
        new Ingredient("Garlic Powder", "1 tablespoon"),
        new Ingredient("Soy Sauce", "1 tablespoon"),
        new Ingredient("Worcestershire Sauce", "1 tablespoon"),
        new Ingredient("Dried Parsley", "1 tablespoon"),
        new Ingredient("Dried Basil", "1 tablespoon"),
        new Ingredient("Dried Oregano", "1 tablespoon"),
        new Ingredient("Dried Rosemary", "0.5 tablespoon"),
        new Ingredient("Salt & Pepper", "To Taste"),
      ]
      )
  ];