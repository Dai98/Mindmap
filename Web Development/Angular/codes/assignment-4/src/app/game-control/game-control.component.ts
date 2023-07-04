import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-game-control',
  templateUrl: './game-control.component.html',
  styleUrls: ['./game-control.component.css']
})
export class GameControlComponent {

  @Output() gameStop: EventEmitter<number[]> = new EventEmitter<number[]>();
  nums: number[] = [];
  interval: any;

  onClickStart() {
    this.interval = setInterval(()=>{this.nums.push(this.nums.length+1)}, 1000);
  }

  onClickStop() {
    clearInterval(this.interval);
    console.log(this.nums);
    if (this.nums.length === 0) {
      return;
    } else {
      this.gameStop.emit(this.nums);
    }
  }

}
