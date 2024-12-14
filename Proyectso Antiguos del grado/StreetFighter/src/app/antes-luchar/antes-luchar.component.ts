import {Component, OnInit} from '@angular/core';
import {PersonajesService} from "../service_personajes/personajes.service";
import {ILuchador} from "../interfaces/i-luchador";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-antes-luchar',
  templateUrl: './antes-luchar.component.html',
  styleUrls: ['./antes-luchar.component.scss']
})
export class AntesLucharComponent implements OnInit{
  personaje: ILuchador[] | any;
  id: number | any;
  random: number | any;
  max: number | any;

  constructor(private route: ActivatedRoute,private cargaPersonajes: PersonajesService) {
  }

  ngOnInit() {
    this.id = this.route.snapshot.params['id'];
    this.random = Math.floor(Math.random() * 6);
    console.log(this.random)
    this.cargaPersonajes.getPersonajes().subscribe(
      personaje => {
        this.personaje = personaje;
      },
      error => console.log(error),
      () => console.log('Fin de observable')
    )
  }
}
