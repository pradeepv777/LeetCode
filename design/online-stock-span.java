import java.util.Stack;

class StockSpanner {

    private Stack<Integer> pricestack;
    private Stack<Integer> spanstack;

    public StockSpanner() {
        pricestack = new Stack<>();
        spanstack = new Stack<>();
    }

    public int next(int price) {
        int span = 1;

        while (!pricestack.isEmpty() && pricestack.peek() <= price) {
            span += spanstack.peek();
            pricestack.pop();
            spanstack.pop();
        }

        pricestack.push(price);
        spanstack.push(span);

        return span;
    }
}
