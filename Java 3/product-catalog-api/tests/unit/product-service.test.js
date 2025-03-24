// This is a starter file - students will complete this
const productService = require('../../src/services/product-service');

describe('ProductService', () => {
  // Sample test to get started
  describe('getAllProducts', () => {
    it('should return all products when no filters are applied', () => {
      const result = productService.getAllProducts();
      expect(result.products.length).toBeGreaterThan(0);
      expect(result).toHaveProperty('total');
      expect(result).toHaveProperty('limit');
      expect(result).toHaveProperty('offset');
    });
    
    describe('getAllProducts', () => {
      it('should return products filtered by category', () => {
        const result = productService.getAllProducts({ category: 'electronics' });
        expect(result.products.length).toBeGreaterThan(0);
        result.products.forEach(product => {
          expect(product.category).toBe('electronics');
        });
      });
    });
    
  });

  describe('getAllProducts', () => {
    it('should return an empty list if no products match the filters', () => {
      const result = productService.getAllProducts({ category: 'nonexistent-category' });
      expect(result.products.length).toBe(0);
    });
  });
  
  
  describe('getAllProducts', () => {
    it('should handle invalid filters gracefully', () => {
      const result = productService.getAllProducts({ category: 'electronics', price: 'invalid' });
      expect(result.products.length).toBeGreaterThan(0);
    });
  });
  
});