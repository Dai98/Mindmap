import { EventEmitter } from "@angular/core";
import { Ingredient } from "../shared/ingredient.model";

export class ShoppingListService {
	ingredientsChanged: EventEmitter<Ingredient[]> = new EventEmitter<Ingredient[]>();

	private ingredients: Ingredient[] = [
		new Ingredient("Apples", "5"),
		new Ingredient("Potato", "10")
	];

	getIngredients() {
		return this.ingredients.slice();
	}

	addIngredient(ingredient: Ingredient) {
		this.ingredients.push(ingredient);
		this.ingredientsChanged.emit(this.ingredients);
	}

	addIngredients(ingredients: Ingredient[]) {
		this.ingredients.push(...ingredients);
		this.ingredientsChanged.emit(this.ingredients);
	}
}