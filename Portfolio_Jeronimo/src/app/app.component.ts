import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BarraNavegacionComponent } from "./barra-navegacion/barra-navegacion.component";
import { FooterComponent } from "./footer/footer.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.scss',
    imports: [RouterOutlet, BarraNavegacionComponent, FooterComponent]
})
export class AppComponent {
  title = 'Portfolio_Jeronimo';
}
