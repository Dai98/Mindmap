import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Recipe Book';

  tabName: string = "recipe";

  onClickMenu(tabName: string) {
    this.tabName = tabName;
  }
}
