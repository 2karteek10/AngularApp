import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-docs',
  standalone: true,
  template: `<h1>Documentation for Project {{ projectId }}</h1>`,
})
export class DocsComponent {
  projectId!: string; // Use '!' for optional initialization

  constructor(private route: ActivatedRoute) {
    this.route.params.subscribe((params) => {
      this.projectId = params['projectId'];
    });
  }
}
