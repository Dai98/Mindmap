import { Component } from '@angular/core';
import { Recipe } from '../recipe.model';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent {
  recipes: Recipe[] = [
    new Recipe(
      "Hamburger",
      "No more dry, lackluster hamburgers. These are juicy, and spices can be easily added or changed to suit anyone's taste. If you find the meat mixture too mushy, just add more bread crumbs until it forms patties that hold their shape. ",
      "https://www.allrecipes.com/thmb/49Srz_vFJmmg40yDTfkoFdb8y7M=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/49404-juiciest-hamburgers-ever-DDMFS-4x3-86fc27c741dd410aa365f96490c54060.jpg"
      )
  ];

  constructor() {}

  ngOnInit() {}

}
