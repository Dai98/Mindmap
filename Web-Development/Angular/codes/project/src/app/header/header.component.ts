import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {

  @Output() clickMenu: EventEmitter<string> = new EventEmitter<string>();

  onSelect(tabName: string) {
    this.clickMenu.emit(tabName);
  }

}
