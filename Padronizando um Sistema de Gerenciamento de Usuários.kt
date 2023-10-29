class User(val id: Int, val name: String)

class UserManager private constructor() {
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

    companion object {
        private var instance: UserManager? = null

        fun getInstance(): UserManager {
            if (instance == null) {
                instance = UserManager()
            }
            return instance as UserManager
        }
    }
}

fun main() {
    println("Enter the number of users:")
    val quantity = readLine()?.toIntOrNull() ?: 0

    val userManager = UserManager.getInstance()

    println("Enter the name of each user:")
    for (i in 1..quantity) {
        val name = readLine() ?: ""
        userManager.addUser(name)
    }

    userManager.listUsers()
}
