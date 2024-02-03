import unittest
import pandas as pd
from revenue_computation import compute_revenue_by_month, compute_revenue_by_product, compute_revenue_by_customer, identify_top_10_customers

class TestRevenueComputation(unittest.TestCase):
    def setUp(self):
        dataSample = {
            'order_id': [1, 2, 3, 4],
            'customer_id': [101, 102, 101, 103],
            'order_date': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15'],
            'product_id': [1, 2, 1, 3],
            'product_name': ['Product A', 'Product B', 'Product A', 'Product C'],
            'product_price': [10, 20, 10, 30],
            'quantity': [2, 1, 3, 1]
        }
        self.testOrder = pd.DataFrame(dataSample)
        

    def test_compute_revenue_by_month(self):
        self.testOrder['order_date'] = pd.to_datetime(self.testOrder['order_date'])
        self.testOrder['month'] = self.testOrder['order_date'].dt.to_period('M')
        expected_result = pd.Series([40, 60], index=pd.period_range('2024-01', periods=2, freq='M'))
        computed_result = compute_revenue_by_month(self.testOrder)
        self.assertTrue(expected_result.equals(computed_result))

    def test_compute_revenue_by_product(self):
        expected_result = pd.Series({'Product A': 50, 'Product B': 20, 'Product C': 30})
        computed_result = compute_revenue_by_product(self.testOrder)
        self.assertTrue(expected_result.equals(computed_result))

    def test_compute_revenue_by_customer(self):
        expected_result = pd.Series({101: 50, 102: 20, 103: 30})
        computed_result = compute_revenue_by_customer(self.testOrder)
        self.assertTrue(expected_result.equals(computed_result))

    def test_identify_top_10_customers(self):
        expected_result = pd.Series({101: 50, 103: 30, 102: 20}).nlargest(10)
        computed_result = identify_top_10_customers(self.testOrder)
        self.assertTrue(expected_result.equals(computed_result))

if __name__ == '__main__':
    unittest.main()
