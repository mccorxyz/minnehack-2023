import 'dart:developer';
import 'dart:convert';

import 'package:http/http.dart' as http;
import 'api_constants.dart';

class ApiService {
  Future<bool?> postBook(String isbn) async {
    try {
      var url = Uri.parse(ApiConstants.baseUrl + ApiConstants.bookEndpoint + isbn);
      var response = await http.post(url);
      log(response.body);
      var parsed = json.decode(response.body);
      var val = parsed['success'].toString();
      return val.toLowerCase() == 'true';
    } catch (e) {
     log(e.toString());
    }
  }
}