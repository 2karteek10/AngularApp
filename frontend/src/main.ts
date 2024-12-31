import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { importProvidersFrom } from '@angular/core';
import { RouterModule } from '@angular/router'; // Import RouterModule for routing
import { LandingPageComponent } from './app/landing-page/landing-page.component';


// Define the routes
const routes = [
  { path: '', component: LandingPageComponent }
];

// Bootstrap the application with routing
bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(RouterModule.forRoot(routes))  // Set up routing with the defined routes
  ]
});
