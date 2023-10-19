package entities;

import java.util.ArrayList;

public class PedidoJogo implements Pedido{

    protected double precoProduto;
    protected ArrayList<PedidoJogo> produtos = new ArrayList<>();

    @Override
    public void addProduto(PedidoJogo produto) {
        produtos.add(produto);
    }

    @Override
    public ArrayList<PedidoJogo> getProdutos() {
        return produtos;
    }

    @Override
    public double calculaValorTotal() {
        precoProduto = 5;
        double precoProdutoTotal = 0;
        int indicePedidos = produtos.size();
        precoProdutoTotal = precoProduto * indicePedidos;
        return precoProdutoTotal;
    }
}
