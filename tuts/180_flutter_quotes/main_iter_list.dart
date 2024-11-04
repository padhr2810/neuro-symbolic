import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
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
        primarySwatch: Colors.blue,
      ),
      home: WeekWidget(),
    );
  }
}

class WeekWidget extends StatefulWidget {
  @override
  _WeekWidgetState createState() => _WeekWidgetState();
}

class _WeekWidgetState extends State<WeekWidget> {
  List weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
  ];

  int index = 0;
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(weekdays[index]),
        ElevatedButton(
          onPressed: () {
            if (index < weekdays.length - 1) {
              setState(() {
                index++;
              });
            } else {
              setState(() {
                index = 0;
              });
            }
          },
          child: Text("Next item"),
        ),
      ],
    );
  }
}
