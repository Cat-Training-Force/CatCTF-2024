#include <stdio.h>

#define Push(n) \
    asm volatile( \
    "pushq %0\n" \
    ::"r"((long long)n) \
    :"rax")

#define Pop() \
    asm volatile( \
    "popq %%rax\n" \
    :"rax")

#define LoadData(n) \
    asm volatile( \
    "movq (%1, %0, 8), %%rax\n" \
    "pushq %%rax\n" \
    ::"r"((long long)n), "r"(buffer) \
    :"rax")

#define StoreData(n) \
    asm volatile( \
    "popq %%rax\n" \
    "movq %%rax, (%1, %0, 8)\n" \
    ::"r"((long long)n), "r"(buffer) \
    :"rax")

#define LoadFlag() \
    asm volatile( \
    "xorq %%rax, %%rax\n" \
    "popq %%rbx\n" \
    "movb (%0, %%rbx, 1), %%al\n" \
    "pushq %%rax\n" \
    ::"r"(flag) \
    :"rax", "rbx")

#define Add() \
    asm volatile( \
    "popq %%rax\n" \
    "addq %%rax, 0(%%rsp)\n" \
    :::"rax")

#define Sub() \
    asm volatile( \
    "popq %%rax\n" \
    "subq %%rax, 0(%%rsp)\n" \
    "negq 0(%%rsp)\n" \
    :::"rax")

#define Xor() \
    asm volatile( \
    "popq %%rax\n" \
    "xorq %%rax, 0(%%rsp)\n" \
    :::"rax")

#define Or() \
    asm volatile( \
    "popq %%rax\n" \
    "orq %%rax, 0(%%rsp)\n" \
    :::"rax")

#define And() \
    asm volatile( \
    "popq %%rax\n" \
    "andq %%rax, 0(%%rsp)\n" \
    :::"rax")

#define Ret(retv) \
    asm volatile( \
    "popq %0\n" \
    :"=r"(retv))

#define SetNotEqual() \
    asm volatile( \
    "popq %%rcx\n" \
    "popq %%rbx\n" \
    "xorq %%rax, %%rax\n" \
    "cmpq %%rcx, %%rbx\n" \
    "setne %%al\n" \
    "pushq %%rax\n" \
    :::"rax", "rbx", "rcx")

#define JumpIf(label) \
    asm goto( \
    "popq %%rax\n" \
    "testq %%rax, %%rax\n" \
    "jnz %l0\n":: \
    :"rax" \
    :label);

enum Var {
    i,
    checked,
    TotalCount
};

volatile long long buffer[TotalCount];
char flag[1024];

long long check()
{
    volatile long long ret_value;

	Push(140);
	Push(13);
	Push(25);
	Push(23);
	Push(223);
	Push(253);
	Push(194);
	Push(21);
	Push(77);
	Push(249);
	Push(12);
	Push(220);
	Push(150);
	Push(218);
	Push(204);
	Push(196);
	Push(3);
	Push(205);
	Push(21);
	Push(64);
	Push(22);
	Push(120);
	Push(97);
	Push(54);
	Push(97);
	Push(222);
	Push(176);
	Push(4);
	Push(155);
	Push(99);
	Push(23);
	Push(10);
	Push(95);
	Push(68);
	Push(208);
	Push(152);
	Push(144);
	Push(197);
	Push(42);
	Push(130);
	Push(125);
	Push(183);
	Push(107);
	Push(182);
	Push(249);
	Push(181);
	Push(78);
	Push(89);
	Push(139);
	Push(252);
	Push(173);
	Push(68);
	Push(74);
	Push(189);
	Push(201);
	Push(233);
	Push(247);
	Push(15);
	Push(131);
	Push(251);
	Push(52);
	Push(200);
	Push(120);
	Push(33);
	Push(198);
	Push(202);
	Push(77);
	Push(176);
	Push(223);
	Push(234);
	Push(189);
	Push(26);
	Push(7);
	Push(40);
	Push(152);
	Push(230);
	Push(57);
	Push(161);
	Push(35);
	Push(170);
	Push(106);
	Push(119);
	Push(31);
	Push(121);
	Push(23);
	Push(29);
	Push(36);
	Push(90);
	Push(142);
	Push(145);
	Push(236);
	Push(35);
	Push(65);
	Push(7);
	Push(39);
	Push(16);
	Push(17);
	Push(45);
	Push(107);
	Push(161);
	Push(209);
	Push(53);
	Push(60);
	Push(194);
	Push(118);
	Push(8);
	Push(112);
	Push(25);
	Push(252);
	Push(84);
	Push(170);
	Push(55);
	Push(0);
	Push(145);
	Push(170);
	Push(104);
	Push(73);
	Push(220);
	Push(136);
	Push(78);
	Push(253);
	Push(3);
	Push(40);
	Push(96);
	Push(102);
	Push(231);
	Push(223);
	Push(148);
	Push(64);
	Push(45);
	Push(7);
	Push(80);
	Push(40);
	Push(190);
	Push(97);
	Push(40);
	Push(216);
	Push(249);
	Push(128);
	Push(217);
	Push(84);
	Push(219);
	Push(132);
	Push(55);
	Push(189);
	Push(228);
	Push(49);
	Push(123);
	Push(249);
	Push(215);
	Push(173);
	Push(236);
	Push(48);
	Push(142);
	Push(255);
	Push(9);
	Push(244);
	Push(141);
	Push(136);
	Push(133);
	Push(137);
	Push(87);
	Push(162);
	Push(211);
	Push(109);
	Push(4);
	Push(81);
	Push(60);
	Push(54);
	Push(44);
	Push(105);
	Push(254);
	Push(89);
	Push(116);
	Push(9);
	Push(119);

    Push(0);
    Push(0);
    StoreData(i);
    StoreData(checked);

begin_loop:
    LoadData(i);
    Push(44);
    SetNotEqual();
    JumpIf(loop);
    LoadData(checked);
    Ret(ret_value);
    return ret_value;

loop:
    LoadData(i);
    LoadFlag();
    Sub();
    Xor();
    Add();
    Push(255);
    And();
    SetNotEqual();
    LoadData(checked);
    Or();
    StoreData(checked);
    LoadData(i);
    Push(1);
    Add();
    StoreData(i);
    Push(1);
    JumpIf(begin_loop);
}

int main(void)
{
    printf("Input your flag:");
    scanf("%100s", flag);

    if (check())
        printf("Wrong!\n");
    else
        printf("Right!\n");
}