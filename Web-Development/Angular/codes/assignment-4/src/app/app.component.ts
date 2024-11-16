import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  oddNums: number[] = [];
  evenNums: number[] = [];

  onGameStop(nums: number[]) {
    for(let num of nums) {
      if (num % 2 !== 0) {
        this.oddNums.push(num);
      } else {
        this.evenNums.push(num);
      }
    }
  }
}
