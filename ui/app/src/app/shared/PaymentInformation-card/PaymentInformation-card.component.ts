import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './PaymentInformation-card.component.html',
  styleUrls: ['./PaymentInformation-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.PaymentInformation-card]': 'true'
  }
})

export class PaymentInformationCardComponent {


}