import { TestBed } from '@angular/core/testing';

import { ResolvePeliculaService } from './resolve-pelicula.service';

describe('ResolvePeliculaService', () => {
  let service: ResolvePeliculaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ResolvePeliculaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
