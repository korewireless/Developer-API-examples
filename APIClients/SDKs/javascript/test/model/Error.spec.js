/*
 * ClientsAPI-Production
 * The Client Management APIs provide a comprehensive set of endpoints for managing clients within the system. These APIs facilitate operations such as creating, retrieving, updating, and deleting client information.
 *
 * OpenAPI spec version: 1.0.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.57
 *
 * Do not edit the class manually.
 *
 */
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.ClientsApiProduction);
  }
}(this, function(expect, ClientsApiProduction) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('Error', function() {
      beforeEach(function() {
        instance = new ClientsApiProduction.Error();
      });

      it('should create an instance of Error', function() {
        // TODO: update the code to test Error
        expect(instance).to.be.a(ClientsApiProduction.Error);
      });

      it('should have the property code (base name: "code")', function() {
        // TODO: update the code to test the property code
        expect(instance).to.have.property('code');
        // expect(instance.code).to.be(expectedValueLiteral);
      });

      it('should have the property message (base name: "message")', function() {
        // TODO: update the code to test the property message
        expect(instance).to.have.property('message');
        // expect(instance.message).to.be(expectedValueLiteral);
      });

    });
  });

}));
