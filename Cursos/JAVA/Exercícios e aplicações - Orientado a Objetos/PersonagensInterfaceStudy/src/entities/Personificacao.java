package entities;

interface Personificacao extends Camuflagem {
    @Override
    void camuflar(int cor);
    void personificar(Heroi heroi);
}
