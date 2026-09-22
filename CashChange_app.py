import 'package:flutter/material.dart';

void main() {
  runApp(const ChangeCalculatorApp());
}

class ChangeCalculatorApp extends StatelessWidget {
  const ChangeCalculatorApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'ทอนเท่าไหร่',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.green,
        ),
        useMaterial3: true,
      ),
      home: const ChangeCalculatorPage(),
    );
  }
}

class ChangeCalculatorPage extends StatefulWidget {
  const ChangeCalculatorPage({super.key});

  @override
  State<ChangeCalculatorPage> createState() =>
      _ChangeCalculatorPageState();
}

class _ChangeCalculatorPageState
    extends State<ChangeCalculatorPage> {
  final TextEditingController priceController =
      TextEditingController();

  final TextEditingController paidController =
      TextEditingController();

  double? change;
  String message = '';

  void calculateChange() {
    final price = double.tryParse(priceController.text);
    final paid = double.tryParse(paidController.text);

    if (price == null || paid == null) {
      setState(() {
        change = null;
        message = 'กรุณากรอกข้อมูลให้ครบถ้วน';
      });
      return;
    }

    if (price < 0 || paid < 0) {
      setState(() {
        change = null;
        message = 'กรุณากรอกจำนวนเงินที่ถูกต้อง';
      });
      return;
    }

    if (paid < price) {
      setState(() {
        change = null;
        message = 'จำนวนเงินที่จ่ายไม่เพียงพอ';
      });
      return;
    }

    setState(() {
      change = paid - price;
      message = '';
    });
  }

  void clearData() {
    setState(() {
      priceController.clear();
      paidController.clear();
      change = null;
      message = '';
    });
  }

  @override
  void dispose() {
    priceController.dispose();
    paidController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF4F8F5),
      appBar: AppBar(
        title: const Text(
          'ทอนเท่าไหร่',
          style: TextStyle(
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.green,
        foregroundColor: Colors.white,
      ),

      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            const SizedBox(height: 15),

            // ไอคอน
            Container(
              width: 90,
              height: 90,
              decoration: BoxDecoration(
                color: Colors.green,
                borderRadius: BorderRadius.circular(25),
              ),
              child: const Icon(
                Icons.payments,
                size: 50,
                color: Colors.white,
              ),
            ),

            const SizedBox(height: 20),

            const Text(
              'คำนวณเงินทอน',
              style: TextStyle(
                fontSize: 28,
                fontWeight: FontWeight.bold,
                color: Colors.green,
              ),
            ),

            const SizedBox(height: 8),

            const Text(
              'กรอกราคาสินค้าและจำนวนเงินที่ลูกค้าจ่าย',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 16,
                color: Colors.grey,
              ),
            ),

            const SizedBox(height: 30),

            // ราคาสินค้า
            TextField(
              controller: priceController,
              keyboardType:
                  const TextInputType.numberWithOptions(
                decimal: true,
              ),
              decoration: InputDecoration(
                labelText: 'ราคาสินค้า',
                hintText: 'เช่น 1350',
                suffixText: 'บาท',
                prefixIcon: const Icon(
                  Icons.shopping_cart,
                ),
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
              ),
            ),

            const SizedBox(height: 15),

            // เงินที่ลูกค้าจ่าย
            TextField(
              controller: paidController,
              keyboardType:
                  const TextInputType.numberWithOptions(
                decimal: true,
              ),
              decoration: InputDecoration(
                labelText: 'เงินที่ลูกค้าจ่าย',
                hintText: 'เช่น 1500',
                suffixText: 'บาท',
                prefixIcon: const Icon(
                  Icons.account_balance_wallet,
                ),
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
              ),
            ),

            const SizedBox(height: 20),

            // ปุ่มคำนวณ
            SizedBox(
              width: double.infinity,
              height: 55,
              child: ElevatedButton.icon(
                onPressed: calculateChange,
                icon: const Icon(Icons.calculate),
                label: const Text(
                  'คำนวณเงินทอน',
                  style: TextStyle(fontSize: 18),
                ),
              ),
            ),

            const SizedBox(height: 10),

            // ปุ่มล้างข้อมูล
            SizedBox(
              width: double.infinity,
              height: 50,
              child: OutlinedButton.icon(
                onPressed: clearData,
                icon: const Icon(Icons.refresh),
                label: const Text('ล้างข้อมูล'),
              ),
            ),

            const SizedBox(height: 25),

            // แสดงข้อความผิดพลาด
            if (message.isNotEmpty)
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.red.shade50,
                  borderRadius: BorderRadius.circular(15),
                  border: Border.all(
                    color: Colors.red.shade200,
                  ),
                ),
                child: Text(
                  message,
                  textAlign: TextAlign.center,
                  style: const TextStyle(
                    color: Colors.red,
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),

            // แสดงเงินทอน
            if (change != null)
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(25),
                decoration: BoxDecoration(
                  color: Colors.green.shade50,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(
                    color: Colors.green,
                    width: 2,
                  ),
                ),
                child: Column(
                  children: [
                    const Icon(
                      Icons.check_circle,
                      color: Colors.green,
                      size: 45,
                    ),

                    const SizedBox(height: 10),

                    const Text(
                      'เงินทอน',
                      style: TextStyle(
                        fontSize: 20,
                        color: Colors.grey,
                      ),
                    ),

                    const SizedBox(height: 5),

                    Text(
                      '${change!.toStringAsFixed(2)} บาท',
                      style: const TextStyle(
                        fontSize: 38,
                        fontWeight: FontWeight.bold,
                        color: Colors.green,
                      ),
                    ),
                  ],
                ),
              ),

            const SizedBox(height: 35),

            const Divider(),

            const SizedBox(height: 10),

            const Text(
              '',
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Colors.grey,
                fontSize: 14,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
