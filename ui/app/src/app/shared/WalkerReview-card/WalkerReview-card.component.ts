import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkerReview-card.component.html',
  styleUrls: ['./WalkerReview-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkerReview-card]': 'true'
  }
})

export class WalkerReviewCardComponent {


}