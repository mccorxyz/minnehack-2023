import 'package:flutter/material.dart';
import 'package:scan/scan.dart';
import 'Api/api_service.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.green,
        scaffoldBackgroundColor: const Color(0xFFF2E8CF)
      ),
      home: const MyHomePage(title: 'Bookend'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String _isbn = '';
  bool? _success;
  String _message = 'Scan an ISBN!';
  final String _welcome = 'Scan a Book\'s Barcode';

  final ScanController _controller = ScanController();

  void _getIsbn(String scan) {
    setState(() {
      _isbn = scan;
    });
  }

  void _resumeScan() {
    _controller.resume();
  }

  void _postBook(String isbn) async {
    _controller.pause();
    _success = await ApiService().postBook(isbn);
    Future.delayed(const Duration(seconds: 1)).then((value) => setState(() {
      _message = 'Book added: $_success';
    }));
  }


  @override
  Widget build(BuildContext context) {

    _controller.pause();

    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset('assets/logo.webp', height: 30,),
            Container(
              padding: const EdgeInsets.all(8.0), child: Text('Bookend')
            )
          ],
        )
      ),
      body: Center(
        child: Column(
          children: [
            Text(_welcome, textScaleFactor: 2,),
            Container(
            width: 500,
            height: 500,
            child: ScanView(
              controller: _controller,
              scanAreaScale: .7,
              scanLineColor: Colors.green.shade400,
              onCapture: (isbn) => _postBook(isbn),
            ),
          ),
        ]),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _resumeScan(),
        child: Text('Scan'),
        backgroundColor: Colors.green,
      ),
    );
  }
}
