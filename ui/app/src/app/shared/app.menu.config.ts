import { MenuRootItem } from 'ontimize-web-ngx';

import { AdministrationCardComponent } from './Administration-card/Administration-card.component';

import { DogCardComponent } from './Dog-card/Dog-card.component';

import { OwnerCardComponent } from './Owner-card/Owner-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { PaymentInformationCardComponent } from './PaymentInformation-card/PaymentInformation-card.component';

import { WalkMonitoringCardComponent } from './WalkMonitoring-card/WalkMonitoring-card.component';

import { WalkRequestCardComponent } from './WalkRequest-card/WalkRequest-card.component';

import { WalkScheduleCardComponent } from './WalkSchedule-card/WalkSchedule-card.component';

import { WalkerCardComponent } from './Walker-card/Walker-card.component';

import { WalkerAvailabilityCardComponent } from './WalkerAvailability-card/WalkerAvailability-card.component';

import { WalkerRateCardComponent } from './WalkerRate-card/WalkerRate-card.component';

import { WalkerReviewCardComponent } from './WalkerReview-card/WalkerReview-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Administration', name: 'ADMINISTRATION', icon: 'view_list', route: '/main/Administration' }
    
        ,{ id: 'Dog', name: 'DOG', icon: 'view_list', route: '/main/Dog' }
    
        ,{ id: 'Owner', name: 'OWNER', icon: 'view_list', route: '/main/Owner' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'PaymentInformation', name: 'PAYMENTINFORMATION', icon: 'view_list', route: '/main/PaymentInformation' }
    
        ,{ id: 'WalkMonitoring', name: 'WALKMONITORING', icon: 'view_list', route: '/main/WalkMonitoring' }
    
        ,{ id: 'WalkRequest', name: 'WALKREQUEST', icon: 'view_list', route: '/main/WalkRequest' }
    
        ,{ id: 'WalkSchedule', name: 'WALKSCHEDULE', icon: 'view_list', route: '/main/WalkSchedule' }
    
        ,{ id: 'Walker', name: 'WALKER', icon: 'view_list', route: '/main/Walker' }
    
        ,{ id: 'WalkerAvailability', name: 'WALKERAVAILABILITY', icon: 'view_list', route: '/main/WalkerAvailability' }
    
        ,{ id: 'WalkerRate', name: 'WALKERRATE', icon: 'view_list', route: '/main/WalkerRate' }
    
        ,{ id: 'WalkerReview', name: 'WALKERREVIEW', icon: 'view_list', route: '/main/WalkerReview' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AdministrationCardComponent

    ,DogCardComponent

    ,OwnerCardComponent

    ,PaymentCardComponent

    ,PaymentInformationCardComponent

    ,WalkMonitoringCardComponent

    ,WalkRequestCardComponent

    ,WalkScheduleCardComponent

    ,WalkerCardComponent

    ,WalkerAvailabilityCardComponent

    ,WalkerRateCardComponent

    ,WalkerReviewCardComponent

];