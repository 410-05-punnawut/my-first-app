import 'package:flutter/material.dart';

void main() {
  runApp(const ChangeCalculator());
}

class ChangeCalculator extends StatelessWidget {
  const ChangeCalculator({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.green,
        ),
        useMaterial3: true,
      ),
      home: const ChangePage(),
    );
  }
}

class ChangePage extends StatefulWidget {
  const ChangePage({super.key});

  @override
  State<ChangePage> createState() => _ChangePageState();
}

class _ChangePageState extends State<ChangePage> {
  final priceController = TextEditingController();
  final paidController = TextEditingController();

  double? change;
  String errorMessage = '';

  void calculate() {
    final price = double.tryParse(priceController.text);
    final paid = double.tryParse(paidController.text);

    setState(() {
      errorMessage = '';

      if (price == null || paid == null) {
        change = null;
        errorMessage = 'กรุณากรอกข้อมูลให้ครบ';
        return;
      }

      if (price < 0 || paid < 0) {
        change = null;
        errorMessage = 'กรุณากรอกจำนวนเงินที่ถูกต้อง';
        return;
      }

      if (paid < price) {
        change = null;
        errorMessage = 'จำนวนเงินที่จ่ายไม่เพียงพอ';
        return;
      }

      change = paid - price;
    });
  }

  void clear() {
    setState(() {
      priceController.clear();
      paidController.clear();
      change = null;
      errorMessage = '';
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
      backgroundColor: const Color(0xFFF5F5F5),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            children: [
              const SizedBox(height: 30),

              const Icon(
                Icons.calculate,
                size: 70,
                color: Colors.green,
              ),

              const SizedBox(height: 30),

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
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              ),

              const SizedBox(height: 15),

              TextField(
                controller: paidController,
                keyboardType:
                    const TextInputType.numberWithOptions(
                  decimal: true,
                ),
                decoration: InputDecoration(
                  labelText: 'เงินที่จ่าย',
                  hintText: 'เช่น 1500',
                  suffixText: 'บาท',
                  prefixIcon: const Icon(
                    Icons.payments,
                  ),
                  filled: true,
                  fillColor: Colors.white,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              ),

              const SizedBox(height: 20),

              SizedBox(
                width: double.infinity,
                height: 52,
                child: ElevatedButton(
                  onPressed: calculate,
                  child: const Text(
                    'คำนวณ',
                    style: TextStyle(fontSize: 18),
                  ),
                ),
              ),

              const SizedBox(height: 10),

              SizedBox(
                width: double.infinity,
                height: 52,
                child: OutlinedButton(
                  onPressed: clear,
                  child: const Text(
                    'ล้าง',
                    style: TextStyle(fontSize: 18),
                  ),
                ),
              ),

              const SizedBox(height: 25),

              if (errorMessage.isNotEmpty)
                Text(
                  errorMessage,
                  style: const TextStyle(
                    color: Colors.red,
                    fontSize: 16,
                  ),
                ),

              if (change != null)
                Container(
                  width: double.infinity,
                  margin: const EdgeInsets.only(top: 10),
                  padding: const EdgeInsets.all(25),
                  decoration: BoxDecoration(
                    color: Colors.green.shade50,
                    borderRadius: BorderRadius.circular(15),
                  ),
                  child: Column(
                    children: [
                      const Text(
                        'เงินทอน',
                        style: TextStyle(
                          fontSize: 20,
                          color: Colors.grey,
                        ),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        '${change!.toStringAsFixed(2)} บาท',
                        style: const TextStyle(
                          fontSize: 36,
                          fontWeight: FontWeight.bold,
                          color: Colors.green,
                        ),
                      ),
                    ],
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
