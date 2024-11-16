import { Component, ElementRef, ViewChild, Output, EventEmitter } from '@angular/core';
import { Ingredient } from 'src/app/shared/ingredient.model';
import { ShoppingListService } from '../shopping-list.service';

@Component({
  selector: 'app-shopping-list-editor',
  templateUrl: './shopping-list-editor.component.html',
  styleUrls: ['./shopping-list-editor.component.css']
})
export class ShoppingListEditorComponent {

  @ViewChild("nameInput") nameInput: ElementRef;
  @ViewChild("amountInput") amountInput: ElementRef;

  name: string;
  amount: string;

  constructor(private shoppingListService: ShoppingListService) {}

  onClickAdd() {
    this.name = this.nameInput.nativeElement.value;
    this.amount = this.amountInput.nativeElement.value;
    
    if (this.name !== '' && this.amount !== '') {
      const ingredient = new Ingredient(this.name, this.amount)
      this.shoppingListService.addIngredient(ingredient);
    } else {
      alert("Please enter both name and amount");
    }
  }

}
