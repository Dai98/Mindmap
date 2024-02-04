import { Component } from "@angular/core";

@Component({
    selector: "app-warning-alert",
    template: "<p>This is a warning alert</p>",
    styles: [
        `
        p {
            padding: 20px;
            background: mistyrose;
            border: 1px solid red;
            color: red;
        }
        `
    ]
})
export class WarningAlertComponent {

}