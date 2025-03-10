/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/03_structs.yml
 *   Object: SimpleStruct
 *   Template: qt6/struct_source.j2
 */
#include <QMetaType>
#include <QDBusMetaType>
#include "SimpleStruct.hpp"
#include "types.hpp"

using namespace gen::structs;

QDBusArgument &gen::structs::operator<<(QDBusArgument &argument, const SimpleStruct &object) {
    argument.beginStructure();
    argument << object.item;
    argument << object.amount;
    argument.endStructure();
    return argument;
}

const QDBusArgument &gen::structs::operator>>(const QDBusArgument &argument, SimpleStruct &object) {
    argument.beginStructure();
    argument >> object.item;
    argument >> object.amount;
    argument.endStructure();
    return argument;
}

bool gen::structs::operator!=(const SimpleStruct &lhs, const SimpleStruct &rhs) {
    return (false
        || lhs.item != rhs.item
        || lhs.amount != rhs.amount
    );
}

SimpleStruct SimpleStructFactory::create (
    Item item,
    uint amount
) const {
    return SimpleStruct {
        .item = item,
        .amount = amount,
    };
}

SimpleStruct SimpleStructFactory::create (
    QVariant item,
    QVariant amount
) const {
    Item member_0;
    member_0 = item.value<Item>();

    uint member_1;
    member_1 = amount.value<uint>();

    return SimpleStruct {
        .item = member_0,
        .amount = member_1,
    };
}