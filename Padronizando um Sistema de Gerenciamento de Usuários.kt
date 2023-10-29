class User(val id: Int, val name: String)

object UserManager {
    private val users = mutableListOf<User>()

    fun addUser(name: String) {
        val id = users.size + 1
        val user = User(id, name)
        users.add(user)
    }

    fun listUsers() {
        println("List of Users:")
        for (user in users) {
            println("${user.id} - ${user.name}")
        }
    }
}

fun main() {
    println("Enter the number of users:")
    val quantity = readLine()?.toIntOrNull() ?: 0

    println("Enter the name of each user:")
    for (i in 1..quantity) {
        val name = readLine() ?: ""
        UserManager.addUser(name)
    }

    UserManager.listUsers()
}
