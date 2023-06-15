import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'assignment-3';

  showDetail: boolean = false;
  detail: string = "Secret Password=Tuna";

  clickLogs: Array<string> = [];

  onShowDetail() {
    this.showDetail = !this.showDetail;
    this.clickLogs.push(new Date() + " " + (this.clickLogs.length + 1) + " click")
  }
}
