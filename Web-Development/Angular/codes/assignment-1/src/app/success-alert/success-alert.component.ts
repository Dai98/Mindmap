import { Component } from "@angular/core";

@Component({
    selector: "app-success-alert",
    templateUrl: "success-alert.component.html",
    styles: [
        `
        p {
            padding: 20px;
            background-color: #ACE1AF;
            border: 1px solid green;
            color: green;
        }
        `
    ]
})
export class SuccessAlertComponent {
    constructor() {}

    ngOnInit() {}
}