import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkMonitoring-card.component.html',
  styleUrls: ['./WalkMonitoring-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkMonitoring-card]': 'true'
  }
})

export class WalkMonitoringCardComponent {


}