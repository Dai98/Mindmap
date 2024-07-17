import { Component, OnInit } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [UserService]
})
export class AppComponent implements OnInit {
  users: {name: string, status: string}[] = [];

  constructor(private service: UserService) {}

  ngOnInit(): void {
    this.users = this.service.users;
  }

  onStatusChange(index: number) {
    this.service.changeUserStatus(index);
  }
}
