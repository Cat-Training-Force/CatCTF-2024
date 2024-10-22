#include <functional>
#include <print>
#include <string>
#include <iostream>

int main()
{
    auto y = ([](auto f)
    {
        return ([](auto x)
        { 
            return x(x);
        }([=](auto y) -> std::function<bool(std::pair<const char*, const char*>)>
        {
            return f([=](auto a)
            {
                return (y(y))(a);
            });
        }));
    });

    auto almost_check = [](auto f)
    {
        return [=](auto n)
        {
            return !*n.first && !*n.second ? true :
                ([](auto a, auto b)
                {
                    return (a & b) | (~a & ~b);
                })(*n.first, 114) != *n.second ? false :
                f(std::pair { n.first + 1, n.second + 1 });
        };
    };

    auto check = y(almost_check);

    std::string flag;
    std::print("Please input the flag:");
    std::getline(std::cin, flag);
    std::println("{}", check({flag.data(), "\xee\xec\xf9\xee\xf9\xeb\xf6\xe8\xbb\xbc\xee\xef\xbe\xef\xb9\xa0\xbe\xef\xbe\xba\xa0\xb9\xe9\xb8\xbf\xa0\xb4\xef\xb8\xe9\xa0\xb8\xb9\xbb\xb4\xbe\xb8\xb9\xee\xee\xba\xbd\xb9\xf0"}) ? "Right!" : "Wrong!");
    return 0;
}