import { Injectable } from "@angular/core";

@Injectable()
export class UserService {
  users: {name: string, status: string}[] = [
    {name: "Max", status: "active"},
    {name: "Anna", status: "active"},
    {name: "Chris", status: "inactive"},
    {name: "Manu", status: "inactive"}
  ];

  changeUserStatus(index: number) {
    let status = this.users[index].status;
    if (status == "active") {
      this.users[index].status = "inactive";
    } else {
      this.users[index].status = "active"
    }
  }
}