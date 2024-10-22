import kotlin.math.pow

@JvmName("\u605f\ua6da\ue59d\u0d28\u89e6\u53a9\u5c35\u1299\u9274\ufbc7\u345f\u42a6\uc0e1\u97fb\u2a49\uaa87")
fun d(input: ByteArray): ByteArray {
    return input.toList().chunked(5).flatMap { chunk ->
        val padding = 5 - chunk.size
        val value = chunk.fold(0L) { acc, c -> acc * 85 + c - 42 } * 85.0.pow(padding).toLong()
        val bytes = ByteArray(4) { i -> ((value shr (24 - i * 8)) and 0xFF).toByte() }
        bytes.take(4 - padding)
    }.toByteArray()
}

fun main() {
    print("Please input flag:")
    val flag = readLine() ?: ""
    if (d(flag.toByteArray()).joinToString("") { "%02x".format(it) } == "b3652c05bda7a487b19bd195098f54c709b990610b63e1650b6d4f42bcb9138221434d") {
        println("Right!")
    } else {
        println("Wrong!")
    }
}
