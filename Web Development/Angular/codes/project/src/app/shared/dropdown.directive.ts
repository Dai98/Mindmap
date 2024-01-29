import { Directive, HostBinding, HostListener, ElementRef } from "@angular/core";

@Directive({
    selector: "[appDropdown]"
})
export class DropdownDirective {

    @HostBinding("class.open") isOpen: boolean = false;

    constructor(private elementRef: ElementRef) {}

    @HostListener("document:click", ['$event']) click(event: Event) {
        this.isOpen = this.elementRef.nativeElement.contains(event.target) ? !this.isOpen : false;
    }
}