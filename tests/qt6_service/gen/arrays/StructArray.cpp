/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.2_arrays_with_structs.yml
 *   Object: StructArray
 *   Template: qt6/struct_source.j2
 */
#include <QMetaType>
#include <QDBusMetaType>
#include "StructArray.hpp"
#include "types.hpp"

using namespace gen::arrays;

QDBusArgument &gen::arrays::operator<<(QDBusArgument &argument, const StructArray &object) {
    argument.beginStructure();
    argument << object.numbers;
    argument.endStructure();
    return argument;
}

const QDBusArgument &gen::arrays::operator>>(const QDBusArgument &argument, StructArray &object) {
    argument.beginStructure();
    argument >> object.numbers;
    argument.endStructure();
    return argument;
}

bool gen::arrays::operator!=(const StructArray &lhs, const StructArray &rhs) {
    return (false
        || lhs.numbers != rhs.numbers
    );
}

StructArray StructArrayFactory::create (
    QList<QList<uint>> numbers
) const {
    return StructArray {
        .numbers = numbers,
    };
}

StructArray StructArrayFactory::create (
    QVariant numbers
) const {
    QList<QList<uint>> member_0;
    for (auto& item_0 : numbers.value<QVariantList>()) {
        QList<uint> o_0;
        for (auto& item_1 : item_0.value<QVariantList>()) {
            uint o_1;
            o_1 = item_1.value<uint>();

            o_0.push_back(o_1);
        }

        member_0.push_back(o_0);
    }

    return StructArray {
        .numbers = member_0,
    };
}