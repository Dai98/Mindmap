import { Component, Output, EventEmitter } from '@angular/core';
import { Recipe } from '../recipe.model';
import { recipes } from './recipe-data';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent {
  recipes: Recipe[] = recipes;
  @Output() clickRecipe: EventEmitter<Recipe> = new EventEmitter<Recipe>();

  onClickRecipe(recipe: Recipe) {
    this.clickRecipe.emit(recipe);
  }

}
