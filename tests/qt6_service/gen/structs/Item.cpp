/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/03_structs.yml
 *   Object: Item
 *   Template: qt6/struct_source.j2
 */
#include <QMetaType>
#include <QDBusMetaType>
#include "Item.hpp"

using namespace gen::structs;

QDBusArgument &gen::structs::operator<<(QDBusArgument &argument, const Item &object) {
    argument.beginStructure();
    argument << object.name;
    argument << object.price;
    argument.endStructure();
    return argument;
}

const QDBusArgument &gen::structs::operator>>(const QDBusArgument &argument, Item &object) {
    argument.beginStructure();
    argument >> object.name;
    argument >> object.price;
    argument.endStructure();
    return argument;
}

bool gen::structs::operator!=(const Item &lhs, const Item &rhs) {
    return (false
        || lhs.name != rhs.name
        || lhs.price != rhs.price
    );
}

Item ItemFactory::create (
    QString name,
    double price
) const {
    return Item {
        .name = name,
        .price = price,
    };
}

Item ItemFactory::create (
    QVariant name,
    QVariant price
) const {
    QString member_0;
    member_0 = name.value<QString>();

    double member_1;
    member_1 = price.value<double>();

    return Item {
        .name = member_0,
        .price = member_1,
    };
}