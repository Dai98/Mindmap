import { Component, ElementRef, ViewChild, Output, EventEmitter } from '@angular/core';
import { Ingredient } from 'src/app/shared/ingredient.model';

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

  @Output() addIngredient: EventEmitter<Ingredient> = new EventEmitter<Ingredient>();

  onClickAdd() {
    this.name = this.nameInput.nativeElement.value;
    this.amount = this.amountInput.nativeElement.value;
    
    if (this.name !== '' && this.amount !== '') {
      const ingredient = new Ingredient(this.name, this.amount)
      this.addIngredient.emit(ingredient);
    } else {
      alert("Please enter both name and amount");
    }
  }

}
