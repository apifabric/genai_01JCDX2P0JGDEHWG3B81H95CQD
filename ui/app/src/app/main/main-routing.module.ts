import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Administration', loadChildren: () => import('./Administration/Administration.module').then(m => m.AdministrationModule) },
    
        { path: 'Dog', loadChildren: () => import('./Dog/Dog.module').then(m => m.DogModule) },
    
        { path: 'Owner', loadChildren: () => import('./Owner/Owner.module').then(m => m.OwnerModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'PaymentInformation', loadChildren: () => import('./PaymentInformation/PaymentInformation.module').then(m => m.PaymentInformationModule) },
    
        { path: 'WalkMonitoring', loadChildren: () => import('./WalkMonitoring/WalkMonitoring.module').then(m => m.WalkMonitoringModule) },
    
        { path: 'WalkRequest', loadChildren: () => import('./WalkRequest/WalkRequest.module').then(m => m.WalkRequestModule) },
    
        { path: 'WalkSchedule', loadChildren: () => import('./WalkSchedule/WalkSchedule.module').then(m => m.WalkScheduleModule) },
    
        { path: 'Walker', loadChildren: () => import('./Walker/Walker.module').then(m => m.WalkerModule) },
    
        { path: 'WalkerAvailability', loadChildren: () => import('./WalkerAvailability/WalkerAvailability.module').then(m => m.WalkerAvailabilityModule) },
    
        { path: 'WalkerRate', loadChildren: () => import('./WalkerRate/WalkerRate.module').then(m => m.WalkerRateModule) },
    
        { path: 'WalkerReview', loadChildren: () => import('./WalkerReview/WalkerReview.module').then(m => m.WalkerReviewModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }