import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Administration-card.component.html',
  styleUrls: ['./Administration-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Administration-card]': 'true'
  }
})

export class AdministrationCardComponent {


}