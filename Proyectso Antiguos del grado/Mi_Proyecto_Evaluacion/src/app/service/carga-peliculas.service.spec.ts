import { TestBed } from '@angular/core/testing';

import { CargaPeliculasService } from './carga-peliculas.service';

describe('CargaPeliculasService', () => {
  let service: CargaPeliculasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CargaPeliculasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
